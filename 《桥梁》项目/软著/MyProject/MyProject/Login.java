package com.example.myproject.login;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.example.myproject.MainActivity;
import com.example.myproject.Mmain;
import com.example.myproject.R;

import java.util.ArrayList;

public class Login extends AppCompatActivity implements View.OnClickListener{
    /**
     * 声明自己写的 DBOpenHelper 对象
     * DBOpenHelper(extends SQLiteOpenHelper) 主要用来
     * 创建数据表
     * 然后再进行数据表的增、删、改、查操作
     */
    private DBOpenHelper mDBOpenHelper;
    private TextView mTvLoginactivityRegister;
    private RelativeLayout mRlLoginactivityTop;
    private EditText mEtLoginactivityUsername;
    private EditText mEtLoginactivityPassword;
    private LinearLayout mLlLoginactivityTwo;
    private Button mBtLoginactivityLogin;
    private CheckBox checkBox;
    private Button mBtLoginAgreement1;
    private Button mBtLoginAgreement2;

    /**
     * 创建 Activity 时先来重写 onCreate() 方法
     * 保存实例状态
     * super.onCreate(savedInstanceState);
     * 设置视图内容的配置文件
     * setContentView(R.layout.activity_login);
     * 上面这行代码真正实现了把视图层 View 也就是 layout 的内容放到 Activity 中进行显示
     * 初始化视图中的控件对象 initView()
     * 实例化 DBOpenHelper，待会进行登录验证的时候要用来进行数据查询
     * mDBOpenHelper = new DBOpenHelper(this);
     */

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        initView();

        mDBOpenHelper = new DBOpenHelper(this);
    }

    /**
     * onCreae()中大的布局已经摆放好了，接下来就该把layout里的东西
     * 声明、实例化对象然后有行为的赋予其行为
     * 这样就可以把视图层View也就是layout 与 控制层 Java 结合起来了
     */
    private void initView() {
        // 初始化控件
        mBtLoginactivityLogin = findViewById(R.id.login_bt_login);
        mTvLoginactivityRegister = findViewById(R.id.login_bt_register);
        //mRlLoginactivityTop = findViewById(R.id.rl_loginactivity_top);
        mEtLoginactivityUsername = findViewById(R.id.xuehao);
        mEtLoginactivityPassword = findViewById(R.id.mima);
        //mLlLoginactivityTwo = findViewById(R.id.ll_loginactivity_two);
        checkBox = findViewById(R.id.login_cb_1);
        mBtLoginAgreement1 = findViewById(R.id.login_bt_1); //用户隐私协议内容跳转按钮
        mBtLoginAgreement2 = findViewById(R.id.login_bt_2);

        // 设置点击事件监听器
        mBtLoginactivityLogin.setOnClickListener(this);
        mTvLoginactivityRegister.setOnClickListener(this);
        mBtLoginAgreement1.setOnClickListener(this);
        mBtLoginAgreement2.setOnClickListener(this);
    }

    public void onClick(View view) {
        switch (view.getId()) {
            // 跳转到注册界面
            case R.id.login_bt_register:
                startActivity(new Intent(this, Regester.class));
                finish();
                break;
            /**
             * 登录验证：
             *
             * 从EditText的对象上获取文本编辑框输入的数据，并把左右两边的空格去掉
             *  String name = mEtLoginactivityUsername.getText().toString().trim();
             *  String password = mEtLoginactivityPassword.getText().toString().trim();
             *  进行匹配验证,先判断一下用户名密码是否为空，
             *  if (!TextUtils.isEmpty(name) && !TextUtils.isEmpty(password))
             *  再进而for循环判断是否与数据库中的数据相匹配
             *  if (name.equals(user.getName()) && password.equals(user.getPassword()))
             *  一旦匹配，立即将match = true；break；
             *  否则 一直匹配到结束 match = false；
             *
             *  登录成功之后，进行页面跳转：
             *
             *  Intent intent = new Intent(this, MainActivity.class);
             *  startActivity(intent);
             *  finish();//销毁此Activity
             */
            case R.id.login_bt_login:
                String name = mEtLoginactivityUsername.getText().toString().trim();
                String password = mEtLoginactivityPassword.getText().toString().trim();
                if (!TextUtils.isEmpty(name) && !TextUtils.isEmpty(password)) {
                    if (checkBox.isChecked()){
                        ArrayList<User> data = mDBOpenHelper.getAllData();
                        boolean match = false;
                        for (int i = 0; i < data.size(); i++) {
                            User user = data.get(i);
                            if (name.equals(user.getName()) && password.equals(user.getPassword())) { //登陆验证逻辑有问题
                                match = true;
                                break;
                            } else {
                                match = false;
                            }
                        }
                        if (match) {
                            Toast.makeText(this, "登录成功", Toast.LENGTH_SHORT).show();
                            Intent intent = new Intent(this, Mmain.class);
                            startActivity(intent);
                            finish();//销毁此Activity
                        } else {
                            Toast.makeText(this, "用户名或密码不正确，请重新输入", Toast.LENGTH_SHORT).show();
                        }
                    } else {
                        Toast.makeText(this, "请勾选同意协议", Toast.LENGTH_SHORT).show();
                    }

                } else {
                    Toast.makeText(this, "请输入你的用户名或密码", Toast.LENGTH_SHORT).show();
                }
                break;
            case R.id.login_bt_1:
                Intent intent_bt_1 = new Intent(Login.this, Agreement.class);
                startActivity(intent_bt_1);
                break;
            case R.id.login_bt_2:
                Intent intent_bt_2 = new Intent(Login.this, Agreement.class);
                startActivity(intent_bt_2);
                break;
        }
    }
}

