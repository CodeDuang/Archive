package com.example.myproject.Fragment;

import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.viewpager.widget.ViewPager;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.GridView;
import android.widget.ImageView;
import android.widget.RadioButton;

import com.example.myproject.R;
import com.example.myproject.seek.GridViewAdapter;
import com.example.myproject.seek.MyViewPagerAdapter;

import java.util.ArrayList;
import java.util.List;

public class SeekFragment extends Fragment {
    private ViewPager vp;
    private RadioButton rb0,rb1,rb2;
    private GridView gridView;

    //适配器
    private MyViewPagerAdapter myViewPagerAdapter;
//    private GridViewAdapter gridViewAdapter;

    private List<ImageView> mImageViews;
//    private List<Object[]> gridview_datas = new ArrayList<Object[]>();

    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    private String mParam1;
    private String mParam2;

    public SeekFragment() {
    }



    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
        }
    }

    private void initData() {
        //下面实例化ImageView的方法，和xml里面写一个ImageView一样，都是创建一个对象。
        ImageView imageView1 = new ImageView(getActivity());
        //给对象传入一个图片源
        imageView1.setImageResource(R.drawable.test1);
        ImageView imageView2 = new ImageView(getActivity());
        //给对象传入一个图片源
        imageView2.setImageResource(R.drawable.test2);
        ImageView imageView3 = new ImageView(getActivity());
        //给对象传入一个图片源
        imageView3.setImageResource(R.drawable.test3);

        //给图片列表对象创建空间
        mImageViews = new ArrayList<>();
        mImageViews.add(imageView1);
        mImageViews.add(imageView2);
        mImageViews.add(imageView3);

        //viewpage监听页面滑动的方法
        vp.addOnPageChangeListener(new ViewPager.OnPageChangeListener() {
            @Override
            public void onPageScrolled(int position, float positionOffset, int positionOffsetPixels) {

            }

            @Override
            public void onPageSelected(int position) {
                //根据显示图片下标，控制圆点的显示与否（注意，我圆点的数量写死了，需要增加图片，一定需要手动增加圆点）
                if(position == 0){
                    rb0.setChecked(true);
                }
                else if(position == 1){
                    rb1.setChecked(true);
                }
                else {
                    rb2.setChecked(true);
                }
            }

            @Override
            public void onPageScrollStateChanged(int state) {

            }
        });
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_seek, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        vp = view.findViewById(R.id.seek_vp);
        rb0 = view.findViewById(R.id.seek_rb_0);
        rb1 = view.findViewById(R.id.seek_rb_1);
        rb2 = view.findViewById(R.id.seek_rb_2);
//        gridView = view.findViewById(R.id.seek_gridView);

        //生成图片（准备数据，放入图片列表中）
        initData();

        //图创建适配器
        myViewPagerAdapter = new MyViewPagerAdapter(mImageViews);
//        gridViewAdapter = new GridViewAdapter(gridview_datas,getActivity());


        //设置Viewpager的适配器
        vp.setAdapter(myViewPagerAdapter);

        //设置gridview适配器
//        gridView.setAdapter(gridViewAdapter);

        //装载gridview数据(随机给的数据)
//        for (int i = 0; i < 48; i++){
//            gridview_datas.add(new Object[]{R.drawable.test1, "欧阳"+i, i , i*10});
//
//        }
    }
}