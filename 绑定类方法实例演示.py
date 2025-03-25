class MyClass:
    existing_attr = "Hello"  # 类属性

    def __init__(self, value=42):
        # 在初始化时调用类方法检查属性
        MyClass.check_and_add_attribute(self, 'new_attr', value)
        # 其他初始化逻辑
        self.other_attr = "Initialized after check"

    @classmethod
    def check_and_add_attribute(cls, obj, attr_name, value):
        """类方法：检查实例是否有某属性，若没有则动态添加"""
        if not hasattr(obj, attr_name):
            setattr(obj, attr_name, value)
            print(f"Added {attr_name} to instance.")
        else:
            print(f"{attr_name} already exists in instance.")

# 测试代码
obj1 = MyClass()
# 输出: Added new_attr to instance.
print(obj1.new_attr)       # 输出: 42
print(obj1.other_attr)     # 输出: Initialized after check

obj2 = MyClass(value=100)
# 输出: Added new_attr to instance.
print(obj2.new_attr)       # 输出: 100

# 测试已有属性
obj3 = MyClass()
obj3.new_attr = "Existing"
obj3 = MyClass()           # 输出: new_attr already exists in instance.
print(obj3.new_attr)       # 输出: Existing（未被覆盖）