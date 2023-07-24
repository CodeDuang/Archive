package com.example.myproject.Fragment;

import android.content.Intent;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.Toast;

import com.example.myproject.MainActivity;
import com.example.myproject.R;
import com.example.myproject.user.RelateApp;
import com.example.myproject.user.Set;
import com.example.myproject.user.UserFeedback;
import com.example.myproject.user.UserMessage;


public class UserFragment extends Fragment implements View.OnClickListener{
    private Button feedback,phone,relate,set,message;



    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    private String mParam1;
    private String mParam2;

    public UserFragment() {

    }


    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_user, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        //一般在onViewCreated下，用view绑定按钮
        feedback = view.findViewById(R.id.user_feedback);
        phone = view.findViewById(R.id.user_phone);
        relate = view.findViewById(R.id.user_relate);
        set = view.findViewById(R.id.user_set);
        message = view.findViewById(R.id.user_message);



        //feedback监听事件
        feedback.setOnClickListener(this);
        phone.setOnClickListener(this);
        relate.setOnClickListener(this);
        set.setOnClickListener(this);
        message.setOnClickListener(this);

    }


    @Override
    public void onClick(View view) {
        int id = view.getId();
        Intent intent = null;
        switch (id){
            case R.id.user_feedback:
                 intent = new Intent(getActivity(), UserFeedback.class);
                 break;
            case R.id.user_phone:
                Toast.makeText(getActivity(),"400-161-9995",Toast.LENGTH_LONG).show();
                break;
            case R.id.user_relate:
                intent = new Intent(getActivity(), RelateApp.class);
                break;
            case R.id.user_set:
                intent = new Intent(getActivity(), Set.class);
                break;
            case R.id.user_message:
                intent = new Intent(getActivity(), UserMessage.class);
                break;

        }
        if(intent != null){
            startActivity(intent);
        }

    }
}