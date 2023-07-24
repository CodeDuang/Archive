package com.example.myproject.login;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.example.myproject.R;

public class Agreement extends AppCompatActivity {
    private Button mBtnLoginAgreementCancle;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_agreement);
        mBtnLoginAgreementCancle = findViewById(R.id.login_agreement_cancel);
        mBtnLoginAgreementCancle.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });
    }
}