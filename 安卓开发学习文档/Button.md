# Button

文字大小、颜色

自定义背景形状

自定义按压效果

点击事件



---

==创建Button跳转新界面的流程：==

1.在放置按钮的布局xml上创建一个Button按钮

2.在MainActivity所在目录下(app/src/main/java/.../)新建一个Activity(注意，不是class，是Activity，安卓的标志，一般选择创建EmptyActivity)：<!--右键目录-New-Activity-EmptyActivity-->

3.找到main目录最下面的AndrMainfest.xml文件，注册新建的Activity（一般已经自动注册好了）

4.进入按钮所在布局的Activity文件，在class下新建一个Button对象（eg：`private Button  bBtnTest`）

5.在onCreate方法里，链接按钮与对应按钮id（eg:`buttonTest = findViewById(R.id.btn_5);`）(btn_5是按钮id)

6.下一行，使用Button的方法设置点击事件（eg：`buttonTest.setOnClickListener(new View.OnClickListener()`）（后面的自动生成）

7.在监听事件的匿名内部类里的onClick方法里，new一个Intend对象，并传参，参数为（原Activity.this，新Activity.class）（eg:`Intent intent = new Intent(ButtonActivity.this,testActivity.class)`）

8.下一行，编辑启动Intent（eg:`startActivity(intent);`）

---

==设定按压效果流程：==

 ##### 新建drawable文件

1.在目录app/src/main/res/drawable文件夹下，右键新建一个Drawable Resource File（Root element目前有：selector（选择器，不同状态下的选择不同的背景）、shape（用于定义view形状）可选）

##### 设置样式（选择shape下）

2.在shape头尖括号内，设定shape样式（eg：`android:shape="rectangle"`）

3.在shape双标签里，可以有样式（corners、solid、stroke等）



##### 设置样式（选择selector下）

（点击效果）

4.在selector双标签内，创建两个<item>双标签，标签头分别设置`state_pressed="true"`

和false（表示点击前，和点击时不同的样式）

5.每个<item>双标签内创建<shape>双标签，在<shape>双标签内写样式，和shape下设置样式相同。

参考代码：

```
<item android:state_pressed="true">
    <shape>
        <solid android:color="#aa6600"/>
        <corners android:radius="5dp"/>
    </shape>
</item>


<item android:state_pressed="false">
    <shape>
        <solid android:color="#FF9900"/>
        <corners android:radius="5dp"/>
    </shape>
</item>
```

##### 使用样式

一般在布局xml里面的用background属性链接对应样式id。

---

==button触法提示事件==

 ##### 设置按钮触法事件（和跳转页面同）

略

##### 提示文本设置

在onClick（View v）方法里，不使用Intent页面切换代码，改用Toast代码。

1.调用makeTest（）方法，参数有三个：.this、文本内容、显示时长

2.在makeTest（）方法后紧接着调用show（）方法（eg：Toast.makeText().show()）

参考代码：

```java
Toast.makeText(EditTextActivity.this,"登陆成功",Toast.LENGTH_SHORT).show();
```



