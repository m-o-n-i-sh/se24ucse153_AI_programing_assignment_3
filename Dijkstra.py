import heapq
import json
import os
import time
import urllib.parse
import urllib.request
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
API_KEY = os.environ.get("GOOGLE_API_KEY")
GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
DISTANCE_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"
CACHE_FILE = "graph_cache.json"
BATCH_SIZE = 10
REQUEST_DELAY = 0.3
DEFAULT_CITIES = [
    "Delhi", "Mumbai", "Chennai", "Kolkata", "Bengaluru",
    "Hyderabad", "Ahmedabad", "Pune", "Jaipur", "Visakhapatnam",
    "Coimbatore","Kochi","Guwahati"
]
def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}, {}
    try:
        with open(CACHE_FILE) as f:
            payload = json.load(f)
        registry = payload.get("city_registry", {})
        graph = {k: [tuple(e) for e in v] for k, v in payload.get("graph", {}).items()}
        return registry, graph
    except Exception:
        return {}, {}

def save_cache(registry, graph):
    with open(CACHE_FILE, "w") as f:
        json.dump({"city_registry": registry, "graph": graph}, f, indent=2)
def _get(url, params):
    query = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{url}?{query}", headers={"User-Agent": "DijkstraIndia/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read().decode())
    except:
        return None
def geocode_city(name):
    data = _get(GEOCODE_URL, {
        "address": f"{name}, India",
        "region": "in",
        "key": API_KEY,
    })
    if not data or data.get("status") != "OK":
        return None
    result = data["results"][0]
    location = result["geometry"]["location"]
    canonical = name.strip().title()
    for comp in result.get("address_components", []):
        if "locality" in comp["types"] or "administrative_area_level_2" in comp["types"]:
            canonical = comp["long_name"]
            break
    return {
        "name": canonical,
        "lat": location["lat"],
        "lon": location["lng"],
        "display": result.get("formatted_address", canonical),
    }
def _distance_batch(origin_names, dest_names):
    data = _get(DISTANCE_URL, {
        "origins": "|".join(f"{n}, India" for n in origin_names),
        "destinations": "|".join(f"{n}, India" for n in dest_names),
        "mode": "driving",
        "region": "in",
        "units": "metric",
        "key": API_KEY,
    })
    if not data or data.get("status") != "OK":
        return None
    matrix = []
    for row in data["rows"]:
        row_km = []
        for elem in row["elements"]:
            if elem.get("status") == "OK":
                row_km.append(round(elem["distance"]["value"] / 1000, 1))
            else:
                row_km.append(None)
        matrix.append(row_km)
    return matrix
def build_graph(city_list):
    names = [c["name"] for c in city_list]
    graph = {n: [] for n in names}
    for i in range(0, len(names), BATCH_SIZE):
        batch_origins = names[i:i+BATCH_SIZE]
        matrix = _distance_batch(batch_origins, names)
        time.sleep(REQUEST_DELAY)
        if matrix is None:
            continue
        for r, src in enumerate(batch_origins):
            for c, dst in enumerate(names):
                if src == dst:
                    continue
                if r < len(matrix) and c < len(matrix[r]):
                    d = matrix[r][c]
                    if d is not None:
                        graph[src].append((dst, d))
    return graph
def dijkstra(graph, start):
    dist = {n: float("inf") for n in graph}
    prev = {n: None for n in graph}
    dist[start] = 0
    heap = [(0, start)]
    seen = set()
    while heap:
        cost, node = heapq.heappop(heap)
        if node in seen:
            continue
        seen.add(node)
        for nei, w in graph.get(node, []):
            new_cost = cost + w
            if new_cost < dist[nei]:
                dist[nei] = new_cost
                prev[nei] = node
                heapq.heappush(heap, (new_cost, nei))
    return dist, prev
def reconstruct_path(prev, target):
    p = []
    while target:
        p.append(target)
        target = prev[target]
    return p[::-1]
def build_default_graph():
    registry = {}
    for raw in DEFAULT_CITIES:
        geo = geocode_city(raw)
        if geo:
            registry[geo["name"]] = geo
        time.sleep(0.1)
    if len(registry) < 2:
        return registry, {}
    graph = build_graph(list(registry.values()))
    save_cache(registry, graph)
    return registry, graph
def action_add(registry, graph):
    names = [n.strip().title() for n in input("City names: ").split(",") if n.strip()]
    added = False
    for n in names:
        if n in registry:
            continue
        geo = geocode_city(n)
        if geo:
            registry[geo["name"]] = geo
            added = True
    if added:
        graph = build_graph(list(registry.values()))
        save_cache(registry, graph)
    return registry, graph
def action_remove(registry, graph):
    n = input("City to remove: ").strip().title()
    if n in registry:
        registry.pop(n)
        graph = build_graph(list(registry.values())) if len(registry) >= 2 else {}
        save_cache(registry, graph)
    return registry, graph
def action_refresh(registry, graph):
    if not registry:
        return build_default_graph()
    graph = build_graph(list(registry.values()))
    save_cache(registry, graph)
    return registry, graph
def action_shortest_path(registry, graph):
    if len(graph) < 2:
        return
    src = input("Source: ").strip().title()
    dst = input("Destination: ").strip().title()
    if src not in graph or dst not in graph or src == dst:
        return
    dist, prev = dijkstra(graph, src)
    if dist[dst] == float("inf"):
        return
    print(dist[dst], "km")
    print(" -> ".join(reconstruct_path(prev, dst)))
def action_all_from(graph):
    if len(graph) < 2:
        return
    src = input("Source: ").strip().title()
    if src not in graph:
        return
    dist, _ = dijkstra(graph, src)
    for city, d in sorted(dist.items()):
        if d != float("inf") and city != src:
            print(city, d)
def action_show(registry):
    for c in registry:
        print(c)
def action_clear(registry, graph):
    if os.path.exists(CACHE_FILE):
        os.remove(CACHE_FILE)
    return {}, {}
def main():
    registry, graph = load_cache()
    if not registry:
        registry, graph = build_default_graph()
    while True:
        print("\n1 Add\n2 Remove\n3 Refresh\n4 Path\n5 All distances\n6 Show\n7 Clear\n8 Exit")
        try:
            ch = int(input("Choice: "))
        except:
            continue
        if ch == 1: registry, graph = action_add(registry, graph)
        elif ch == 2: registry, graph = action_remove(registry, graph)
        elif ch == 3: registry, graph = action_refresh(registry, graph)
        elif ch == 4: action_shortest_path(registry, graph)
        elif ch == 5: action_all_from(graph)
        elif ch == 6: action_show(registry)
        elif ch == 7: registry, graph = action_clear(registry, graph)
        elif ch == 8: break
if __name__ == "__main__":
    main()