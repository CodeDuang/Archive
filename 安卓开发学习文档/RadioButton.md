# RadioButton
*（解释：单选按钮，一般放在RadioGroup里实现单选）*

---



## 属性
checked :默认选中该项(eg:`android:checked="true"` :设为默认选择)
button:对选择框进行更改（eg:`android:button="@null"` ：不显示选择框）



## 使用样例（一般放到RadioGroup里）
```xml
    <RadioGroup
        android:id="@+id/rg_1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:orientation="vertical">
        <RadioButton
            android:id="@+id/rb_1"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"

            android:text="男"
            android:textSize="16sp"
            android:textColor="#FF6600"

            android:checked="true"/>
        <RadioButton
            android:id="@+id/rb_2"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"

            android:text="女"
            android:textSize="16sp"
            android:textColor="#FF6600"/>
    </RadioGroup>
```

## 活动代码

监听器：setOnCheckedChangeListener（new RadioGroup.OnCheckedChangeListener(){...}）

... :  public void onCheckedChanged(RadioGroup radioGroup, int i) {}

```java
RadioGroup rg1;
rg1 = findViewById(R.id.rg_1);
rg1.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
    @Override
    public void onCheckedChanged(RadioGroup radioGroup, int i) {
        android.widget.RadioButton radioButton = radioGroup.findViewById(i);
        Toast.makeText(RadioButton.this,radioButton.getText(),Toast.LENGTH_SHORT).show();

    }
});
```

