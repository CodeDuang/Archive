package com.example.myproject.seek;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
//import androidx.recyclerview.widget.RecyclerView;

import com.example.myproject.R;

import java.util.List;

public class GridViewAdapter extends BaseAdapter {
    //建立头像列表[0]、姓名列表[1]、咨询次数列表[2]、好评列表[3]
//    private List<ImageView> datas_image;
//    private List<String> datas_name;
//    private List<Integer> datas_time;
//    private List<Float> datas_good;
    private List<Object[]> datas;
    private Context context;

    //构造函数
    public GridViewAdapter(List<Object[]> datas, Context context) {
        this.datas = datas;
        this.context = context;
    }


    //列表里面的数据个数
    @Override
    public int getCount() {
        return datas.size();
    }

    //返回列表中对应下标的数据对象
    @Override
    public Object getItem(int i) {
        return datas.get(i);
    }

    @Override
    public long getItemId(int i) {
        return i;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        ViewHolder holder;
        if (view == null){
            holder = new ViewHolder();
            //将定义好的模板xml布局，转化为view，以供引用
            view = LayoutInflater.from(context).inflate(R.layout.item_seek_teacher,viewGroup,false);

            //以”view“为中介，绑定holder的属性与定义的item模板组件
            holder.head = view.findViewById(R.id.seek_teacher_head);
            holder.name = view.findViewById(R.id.seek_teacher_name);
            holder.time = view.findViewById(R.id.seek_teacher_time);
            holder.good = view.findViewById(R.id.seek_teacher_good);

            //将holder缓存至view
            view.setTag(holder);
        }else {
            //如果已经有view，则取出缓存的holder
            holder = (ViewHolder) view.getTag();

        }
        //赋值头像图片id,名字，咨询次数，好评
        holder.head.setImageResource((int)datas.get(i)[0]);
        holder.name.setText((String)datas.get(i)[1]);
        holder.time.setText((String)datas.get(i)[2]);
        holder.good.setText((String)datas.get(i)[3]);
        return view;
    }

    class ViewHolder{
        //头像、姓名、咨询次数、好评
        ImageView head;
        TextView name,time,good;
    }
}