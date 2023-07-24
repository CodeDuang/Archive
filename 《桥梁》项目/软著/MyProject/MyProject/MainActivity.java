package com.example.myproject;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;

import com.example.myproject.login.Login;

import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends AppCompatActivity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Intent intent = new Intent(MainActivity.this, Login.class);

        Timer timer = new Timer(); //创建定时对象
        TimerTask task = new TimerTask() {
            @Override
            public void run() { //执行
                startActivity(intent);
            }
        };

        timer.schedule(task, 1000*1); //1s后



    }
}