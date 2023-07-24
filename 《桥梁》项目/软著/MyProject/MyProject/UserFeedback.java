package com.example.myproject.user;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RatingBar;
import android.widget.Toast;

import com.example.myproject.R;

public class UserFeedback extends AppCompatActivity {

    private RatingBar ratingBar;
    private EditText editText;
    private Button button,back;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_feedback);

        //分别绑定 打星  反馈文本框   提交按钮
        ratingBar = findViewById(R.id.user_feedback_star);
        editText = findViewById(R.id.user_feedback_input);
        button = findViewById(R.id.user_feedback_submit);
        back = findViewById(R.id.user_feedback_btn_back);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //点击提交事件
                Toast.makeText(getApplicationContext(),"提交成功",Toast.LENGTH_SHORT).show();
            }
        });

        ratingBar.setOnRatingBarChangeListener(new RatingBar.OnRatingBarChangeListener() {
            @Override
            public void onRatingChanged(RatingBar ratingBar, float v, boolean b) {
                if(b){
                    String s = Float.toString(v);
                    Toast.makeText(getApplicationContext(),"点了"+v,Toast.LENGTH_SHORT).show();
                }
            }
        });
        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });


    }
}