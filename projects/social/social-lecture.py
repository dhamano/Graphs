import random, sys

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.queue = None
        self.size_of_queue = 0

    def enqueue(self, value):
        llEl = LinkedList(value)
        self.size_of_queue += 1
        if self.queue is None:
            self.queue = llEl
        else:
            el = self.queue
            if el.next is None:
                el.next = llEl
            else:
                while el.next is not None:
                    el = el.next
                el.next = llEl

    def dequeue(self):
        el = self.queue
        self.size_of_queue -= 1
        if el is not None:
            self.queue = el.next
        return el

    def size(self):
        return self.size_of_queue

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Check if avg_friendships is valid for num_users
        if avg_friendships >= num_users:
            # raise ValueError("avg_friendships cannot be equal or greater then num_users").with_traceback(sys.exc_info()[2])
            raise ValueError("avg_friendships cannot be equal or greater then num_users")
        
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # 100 users, avg 10 friendships each
        # avg_friendships = total_friendships / num_users
        # 2 = total_friendships / 10
        # total_friendships = 20
        # total_friendships = avg_friendships * num_users

        # Add users
        # Time Complexity: O(n)
        for i in range(num_users):
            self.add_user(f"User {i+1}")
        # print("self.users", self.users)

        # Create friendships
        # total_friendships = avg_friendships * num_users

        # Create a list with all possible friendship combinations,
        possible_friendships = []
        # print("possible_friendships",possible_friendships)
        # Time Complexity: O(n^2)
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                # print("friend_id", friend_id, "user_id", user_id, "last_id", self.last_id)
                possible_friendships.append( (user_id, friend_id) )
            
        # print("\n~~~~\npossible_friendships",possible_friendships)
        
        # print(possible_friendships)
        # print(len(possible_friendships))

        # shuffle the list
        # Time Complexity: O(n)
        random.shuffle(possible_friendships)

        # print("\n~~~~\nrandom possible_friendships", possible_friendships)

        # then grab the first N elements from the list.
        # Number of times to call add_friendships = avg_friendships * num_users / 2
        # Time Complexity: O(n*k)
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
        # print("\n~~~~\nfriendship", self.friendships)

    def populate_graph_random_sampling(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add Users
        # Time complexity: O(n)
        for i in range(num_users):
            self.add_user(f"User {i+1}")
        
        # Create friendships
        target_friendships = avg_friendships * num_users
        total_friendships = 0
        collisions = 0

        # While number of friendships < avg_friendships * num_users / 2
        while total_friendships < target_friendships:
            # Pick two random users
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            # Try to create the friendship
            # self.add_friendship(user_id, friend_id)
            # If it fails, try again
            if self.add_friendship(user_id, friend_id):
                total_friendships += 1
            else:
                collisions += 1
        print("COLLISIONS:", collisions)


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Create a queue
        q = Queue()
        # Enqueue a path to the starting user
        q.enqueue( [user_id] )
        # Create a dictionary to store visited users
        visited = {} # Note that this is a dictionary not a set
        # While the queue is not empty:
        while q.size() > 0:
            # Dequeue the first social path
            path = q.dequeue()
            # Grab the last user from the social path
            u = path.value[-1]
            # If it has not been visited:
            if u not in visited:
                # Add it to the visited dictionary with the path as the value
                visited[u] = path.value
                # Then enqueue paths to each neighbor
                for friend in self.friendships[u]:
                    path_copy = path.value.copy()
                    path_copy.append(friend)
                    q.enqueue(path_copy)

        return visited

import time
if __name__ == '__main__':
    sg = SocialGraph()
    # sg.populate_graph(100, 20)
    # sg.populate_graph_random_sampling(10,2)
    # print("---")
    # print("users\n",sg.users)
    # print("---")
    # print("friendships\n",sg.friendships)
    # print("---")
    # connections = sg.get_all_social_paths(1)
    # print("connections\n",connections)
    num_users = 400
    avg_friendships = 300

    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph(num_users, avg_friendships)
    end_time = time.time()
    print("~~~~")
    print(f"Populate graph: {end_time - start_time} sec")
    
    print("\n\n~~~~")
    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph_random_sampling(num_users, avg_friendships)
    end_time = time.time()
    print(f"Populate graph: {end_time - start_time} sec")