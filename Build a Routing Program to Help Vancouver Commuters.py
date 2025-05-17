from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

def get_station_from_landmark():
    # Display the landmark choices for the user
    print("Select a landmark to start:")
    for letter, landmark in landmark_choices.items():
        print(f"{letter}: {landmark}")

    start_letter = input("Enter the letter for your starting landmark: ").upper()
    start_landmark = landmark_choices.get(start_letter)

    if not start_landmark:
        print("Invalid choice. Please try again.")
        return get_station_from_landmark()

    # Get corresponding metro stations for the selected landmark
    start_station = vc_landmarks.get(start_landmark)
    return start_station, start_landmark

def main():
    print("Welcome to SkyRoute!")
    
    # Get starting landmark and station
    start_station, start_landmark = get_station_from_landmark()

    # Prompt the user to select the destination landmark
    print("\nSelect a landmark to reach:")
    for letter, landmark in landmark_choices.items():
        print(f"{letter}: {landmark}")

    end_letter = input("Enter the letter for your destination landmark: ").upper()
    end_landmark = landmark_choices.get(end_letter)

    if not end_landmark:
        print("Invalid choice. Please try again.")
        return main()

    # Get corresponding metro stations for the destination landmark
    end_station = vc_landmarks.get(end_landmark)

    # Perform BFS or DFS to find the route
    print("\nSearching for a route using BFS...")
    bfs_path = bfs(vc_metro, start_station, end_station)
    if bfs_path:
        print(f"Route found using BFS: {' -> '.join(bfs_path)}")
    else:
        print("No route found using BFS.")

    print("\nSearching for a route using DFS...")
    dfs_path = dfs(vc_metro, start_station, end_station)
    if dfs_path:
        print(f"Route found using DFS: {' -> '.join(dfs_path)}")
    else:
        print("No route found using DFS.")

if __name__ == "__main__":
    main()
