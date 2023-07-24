package com.example.myproject;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.RadioGroup;

import com.example.myproject.Fragment.HeartFragment;
import com.example.myproject.Fragment.InformationFragment;
import com.example.myproject.Fragment.SeekFragment;
import com.example.myproject.Fragment.UserFragment;
import com.example.myproject.heart.AddActivity;
import com.example.myproject.Fragment.TreeFragment;

public class Mmain extends AppCompatActivity implements RadioGroup.OnCheckedChangeListener{


    RadioGroup radioGroup;
//    声明四个按钮对应的Fragment对象
    Fragment seek, tree, heart, user, information;
    private FragmentManager manager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_mmain);

        radioGroup = findViewById(R.id.main_rg);
//        设置监听了哪个按钮
        radioGroup.setOnCheckedChangeListener(this::onCheckedChanged);

//      创建碎片对象
        seek = new SeekFragment();
        tree = new TreeFragment();
        heart = new HeartFragment();
        user = new UserFragment();
        information = new InformationFragment();
//      将四个碎片动态加载到布局中  。replace 或 add/hide/show  (本次使用前者)
        addFragmentPage();




    }

    /**
     * @des 将主页当中的碎片一起加载进入布局，有用的显示，暂时无用的隐藏
     */
    private void addFragmentPage() {
//      1.创建碎片管理者对象
        manager = getSupportFragmentManager();
//      2.创建碎片处理事务的对象
        FragmentTransaction transaction = manager.beginTransaction();
//      3.将四个Fragment碎片统一的添加到布局当中(不是，舍弃了add，换成了replace)
        transaction.replace(R.id.main_layout_center,seek); //首页显示seek页面

//      5.提交改变后的事务
        transaction.commit();

    }

    @Override
    public void onCheckedChanged(RadioGroup radioGroup, int i) {
        FragmentTransaction transaction = manager.beginTransaction();
        switch (i){
            case R.id.main_rb_seek:
                transaction.replace(R.id.main_layout_center,seek);
                break;
            case R.id.main_rb_tree:
                transaction.replace(R.id.main_layout_center,tree);
                break;
            case R.id.main_rb_heart:
                transaction.replace(R.id.main_layout_center,heart);
                break;
            case R.id.main_rb_user:
                transaction.replace(R.id.main_layout_center,user);
                break;
            case R.id.main_rb_information:
                transaction.replace(R.id.main_layout_center,information);
                break;
        }
        transaction.commit();

    }

    //这是HeartFrament碎片内的一个按钮方法，在heart。xml里面声明的
    public void add(View view) {
        Intent intent = new Intent(Mmain.this, AddActivity.class);
        startActivity(intent);
    }
}