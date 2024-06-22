class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        
    # __repr__ is used to return an string for other developers with a more complex description of the class
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    # __str__is used to return a straight forward description of the class with the target of the client in mind
    def __str__(self):
        return self.__repr__()
    

class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        # this method insert is a built in python method for list objects different from the UserDatabase class insert method, it does not throw error if the index is out of range    
        # instead if the given index it's out of range it appends the number in the nearest position of the one we indicated
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        
    def list_all(self):
        return self.users

# binary tree basic structure
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None        


node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)


node0.left = node1
node0.right = node2