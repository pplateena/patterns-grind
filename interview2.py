"""
Написать класс Друзья, с методами init(friendship) (добавить список друзей),
add_friends(friendship),
remove_friends(friendship),
return_friends(a) -возвращает список друзей определенного человека.
Friendship переменная типа set(множество) (например ('Ваня',' Дима')).
Если есть такая переменная - значит Ваня дружит с Димой
"""

class Friends:
    def __init__(self):
        self.friendship = set()
    def add_friends(self, friend_tuple):
        ordered_tuple = tuple(sorted(list(friend_tuple)))
        self.friendship.add((ordered_tuple))
    def remove_friends(self, friend_tuple):
        ordered_tuple = tuple(sorted(list(friend_tuple)))
        self.friendship.discard(ordered_tuple)
    def return_friends(self,checked_friend):
        output = []
        for pair in self.friendship:
            if checked_friend == pair[0] or checked_friend == pair[1]:
                if checked_friend == pair[0]:
                    output.append(pair[1])
                else:
                    output.append(pair[0])
        return output

friends = Friends()

friends.add_friends(('Alex', 'Jack'))
friends.add_friends(('Alex', 'Jack'))
friends.add_friends(('Jack','Alex'))
friends.add_friends(('Alex', 'Arsen'))

friendsOfAlex = friends.return_friends('Alex')
print(friendsOfAlex)

friends.add_friends(('Jack', 'Arsen'))
friendsOfJack = friends.return_friends('Jack')
print(friendsOfJack)

friends.remove_friends(('Jack', 'Arsen'))
friendsOfJack = friends.return_friends('Jack')
print(friendsOfJack, 'after removal')