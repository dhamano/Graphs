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
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

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
        # print("self.users", self.users)
        for i in range(num_users):
            self.add_user(f"User {i+1}")
        # print("self.users", self.users)

        # Create friendships
        # total_friendships = avg_friendships * num_users

        # Create a list with all possible friendship combinations,
        possible_friendships = []
        # print("possible_friendships",possible_friendships)
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id +1):
                possible_friendships.append( (user_id, friend_id) )
        # print("\n~~~~\npossible_friendships",possible_friendships)
        
        # print(possible_friendships)
        # print(len(possible_friendships))

        # shuffle the list
        random.shuffle(possible_friendships)

        # print("\n~~~~\nrandom possible_friendships", possible_friendships)

        # then grab the first N elements from the list.
        # Number of times to call add_friendships = avg_friendships * num_users / 2
        # print("\n~~~~\nfriendship", self.friendships)
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
        # print("\n~~~~\nfriendship", self.friendships)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue( [user_id] )

        while q.size() > 0:
            # print("\n\n~~~~~~")
            p = q.dequeue()
            v = p.value[-1]
            # print("user's friendships", self.friendships[v])
            friends_of_user_id = self.friendships[v]
            for friend in friends_of_user_id:
                if friend not in visited and friend != user_id:
                    # print("adding to visited", friend)
                    cp = p.value.copy()
                    # print("copy", cp, type(cp))
                    cp.append(friend)
                    # print("copy append", cp)
                    q.enqueue(cp)
                    visited[friend] = cp
                    # print("visited", visited)
            # print("add!", visited)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 5)
    print("---")
    print("users",sg.users)
    print("---")
    print("friendships",sg.friendships)
    print("---")
    connections = sg.get_all_social_paths(1)
    print("connections",connections)
    