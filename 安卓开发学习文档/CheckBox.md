# CheckBox

*(解释:复选框)* 

---

##  常用属性
button:对前方选择框操作(eg:`android:button="@drawable/bg_checkbox`")



## 监听事件

监听器：`setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener(){...})`

... : `public void onCheckedChanged(CompoundButton compoundButton, boolean b){}`

```java
CheckBox mCb1;
mCb1 = (CheckBox) findViewById(R.id.cb_1);
mCb1.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
    @Override
    public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
        Toast.makeText(CheckBoxActivity.this,b?"1选中":"1未选中",Toast.LENGTH_SHORT).show();
    }
});
```

