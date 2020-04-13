package com.example.myapplication.selectTime;

import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

import com.example.myapplication.R;

public class DayTimeViewHolder extends RecyclerView.ViewHolder{

    public TextView select_txt_day;      //日期文本
    public LinearLayout select_ly_day;       //父容器 ， 用于点击日期

    public DayTimeViewHolder(View itemView) {
        super(itemView);
        select_ly_day = (LinearLayout) itemView.findViewById(R.id.select_ly_day);
        select_txt_day = (TextView) itemView.findViewById(R.id.select_txt_day);
    }
}
