# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


from string import whitespace


firstGoal = 'Ruud Gullit'
secondGoal = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = firstGoal + ' ' + str(goal_0)+', ' + secondGoal + ' ' + str(goal_1)
report = f'{firstGoal} scored in the {goal_0}nd minute\n' f'{secondGoal} scored in the {goal_1}th minute'

player = 'Ronald Koeman'
first_name = player[player.find('Ronald'):6]
last_name_len = len(player[7:])
name_short = f'{first_name[0]}.{player[last_name_len:]}'
x = len(first_name)
withoutspace = f'{first_name}! ' * x
chant = withoutspace.rstrip()
good_chant = withoutspace != chant
print(scorers) 
print(report)
print(chant)
print(good_chant)



