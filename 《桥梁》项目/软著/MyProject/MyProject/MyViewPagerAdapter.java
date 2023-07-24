package com.example.myproject.seek;

import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import androidx.annotation.NonNull;
import androidx.viewpager.widget.PagerAdapter;

import java.util.List;

public class MyViewPagerAdapter extends PagerAdapter {

    private List<ImageView> mImageViewsList;

    public MyViewPagerAdapter(List<ImageView> mImageViewsList) {
        this.mImageViewsList = mImageViewsList;
    }

    @Override
    public int getCount() {
        return mImageViewsList == null?0:mImageViewsList.size();
    }

    @Override
    public boolean isViewFromObject(@NonNull View view, @NonNull Object object) {
        return view == object;
    }

    @NonNull
    @Override
    public Object instantiateItem(@NonNull ViewGroup container, int position) {
        //获取对应下标的图片
        ImageView imageView = mImageViewsList.get(position);

        //获取的图片加入viewpage主页面
        container.addView(imageView);

        //返回获取的图片
        return imageView;
    }

    //当图片被划走，销毁该图片
    @Override
    public void destroyItem(@NonNull ViewGroup container, int position, @NonNull Object object) {
//        super.destroyItem(container, position, object); 这段一定要去掉
        container.removeView((View) object);
    }
}
