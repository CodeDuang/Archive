# TextView

## 可实现样式：
文字大小、颜色
显示不下使用... ：ellipsize="end"   （一般1配合maxLines控制行数使用）
文字+icon
中划线、下划线(需要调整java代码)
跑马灯效果(需要加入如下代码):

```xaml
android:singleLine="true"
android:ellipsize="marquee"
android:marqueeRepeatLimit="marquee_forever"
android:focusable="true"
android:focusableInTouchMode="true"
```

