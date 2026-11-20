class Father:
    def __init__(self, skill1, **kwargs):
        super().__init__(**kwargs)
        self.skill1 = skill1


class Mother:
    def __init__(self, skill2, **kwargs):
        super().__init__(**kwargs)
        self.skill2 = skill2


class Child(Father, Mother):
    def __init__(self, skill1, skill2, skill3):
        super().__init__(skill1=skill1, skill2=skill2)
        self.skill3 = skill3


c = Child("Gardening", "Knitting", "Studying")
print(c.skill1)
print(c.skill2)
print(c.skill3)


# class Father:
#     def __init__(self, father_skill):
#         self.father_skill = father_skill
#         print("Father's constructor called")

# class Mother:
#     def __init__(self, mother_skill):
#         self.mother_skill = mother_skill
#         print("Mother's constructor called")

# class Child(Father, Mother):
#     def __init__(self, f_skill, m_skill, c_skill):
#         # 1. Explicitly call Father's constructor
#         Father.__init__(self, f_skill)

#         # 2. Explicitly call Mother's constructor
#         Mother.__init__(self, m_skill)

#         # 3. Initialize Child's own attribute
#         self.child_skill = c_skill
#         print("Child's constructor called")

# # Create an instance of Child
# kid = Child("Coding", "Cooking", "Gaming")

# print(f"Skills: {kid.father_skill}, {kid.mother_skill}, {kid.child_skill}")
