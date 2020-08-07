"""
基于原型(Prototype)的编程

也是面向对象编程的一种方式。没有 class 化的，直接使用对象。又叫，基于实例的编程。
其主流的语言就是 JavaScript，与传统的面向对象编程的比较如下：

- 在基于类的编程当中，对象总共有两种类型。类定义了对象的基本布局和函数特性，而接口是“可以使用的”对象，它基于特定类的样式。在此模型中，类表现为行为和结构的集合，对所有接口来说这些类的行为和结构都是相同的。因而，区分规则首先是基于行为和结构，而后才是状态。
- 原型编程的主张者经常争论说，基于类的语言提倡使用一个关注分类和类之间关系的开发模型。与此相对，原型编程看起来提倡程序员关注一系列对象实例的行为，而之后才关心如何将这些对象划分到最近的使用方式相似的原型对象，而不是分成类。
- 在基于类的语言中，一个新的实例通过类构造器和构造器可选的参数来构造，结果实例由类选定的行为和布局创建模型。
- 在基于原型的系统中构造对象有两种方法，通过复制已有的对象或者通过扩展空对象创建。很多基于原型的系统提倡运行时进行原型的修改，而基于类的面向对象系统只有动态语言允许类在运行时被修改。

以 JavaScript 的原型为例：
基于原型编程，直接在对象上改，基于编程的修改，直接对类型进行修改。
每个对象都有一个 __proto__ 的属性，这个就是“原型”。如果把 foo 赋值给 bar.__proto__，那就意味着，bar 的原型就成了 foo 的。

- __proto__ 主要是安放在一个实际的对象中，用它来产生一个链接，一个原型链，用于寻找方法名或属性，等等。
- prototype 是用 new 来创建一个对象时构造 __proto__ 用的。它是构造函数的一个属性。

在 JavaScript 中，对象有两种表现形式，一种是 object，一种是 Function。
我们可以简单地认为，__proto__ 是所有对象用于链接原型的一个指针，而 prototype 则是 Function 对象的属性，其主要是用来当需要 new 一个对象时让 __proto__ 指针所指向的地方。对于超级对象 Function 而言，Function.__proto__ 就是 Function.prototype。
"""