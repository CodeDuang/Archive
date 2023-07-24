package com.example.myproject.user;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.example.myproject.R;

public class Set extends AppCompatActivity implements View.OnClickListener {
    private Button back;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_set);
        back = findViewById(R.id.user_set_btn_back);
        back.setOnClickListener(this);

    }

    @Override
    public void onClick(View view) {
        int id = view.getId();
        switch (id){
            case R.id.user_set_btn_back:
                finish();
                break;
        }
    }
}