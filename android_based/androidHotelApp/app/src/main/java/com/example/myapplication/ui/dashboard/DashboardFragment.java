package com.example.myapplication.ui.dashboard;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.myapplication.MonthTimeAdapter;
import com.example.myapplication.R;
import com.example.myapplication.entity.DayTimeEntity;
import com.example.myapplication.entity.MonthTimeEntity;
import com.example.myapplication.entity.UpdataCalendar;
import com.example.myapplication.select_room;

import java.util.ArrayList;
import java.util.Calendar;

import de.greenrobot.event.EventBus;

public class DashboardFragment extends Fragment {

    private ImageButton back;
    private TextView startTime;          //开始时间
    private TextView stopTime;           //结束时间

    private RecyclerView reycycler;
    private MonthTimeAdapter adapter;
    private ArrayList<MonthTimeEntity> datas;

    private String startT;
    private String stopT;

    public static DayTimeEntity startDay;
    public static DayTimeEntity stopDay;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        View root = inflater.inflate(R.layout.fragment_dashboard, container, false);

        startTime = (TextView) root.findViewById(R.id.plan_time_txt_start);
        stopTime = (TextView) root.findViewById(R.id.plan_time_txt_stop);

        reycycler = (RecyclerView) root.findViewById(R.id.plan_time_calender);
        LinearLayoutManager layoutManager =
                new LinearLayoutManager(getActivity(),   // 上下文
                        LinearLayout.VERTICAL,  //垂直布局,
                        false);

        reycycler.setLayoutManager(layoutManager);
        initView();
        initData();

        EventBus.getDefault().register(this);

        Button confirm = root.findViewById(R.id.button);
        confirm.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getActivity(), select_room.class);
                startT = startTime.getText().toString();
                startT = startT.replaceAll("\n","");
                stopT = stopTime.getText().toString();
                stopT = stopT.replaceAll("\n","");
                intent.putExtra("startTime",startT);
                intent.putExtra("stopTime",stopT);
                startActivity(intent);
            }
        });



        return root;
    }

    private void initData() {
        startDay = new DayTimeEntity(0,0,0,0);
        stopDay = new DayTimeEntity(-1,-1,-1,-1);
        datas = new ArrayList<>();

        Calendar c = Calendar.getInstance();
        int year = c.get(Calendar.YEAR);
        int month = c.get(Calendar.MONTH)+1;

        c.add(Calendar.MONTH,1);
        int nextYear = c.get(Calendar.YEAR);
        int nextMonth = c.get(Calendar.MONTH)+1;

        c.add(Calendar.MONTH,1);
        int nextYear2 = c.get(Calendar.YEAR);
        int nextMonth2 = c.get(Calendar.MONTH)+1;

        datas.add(new MonthTimeEntity(year,month));                //当前月份
        datas.add(new MonthTimeEntity(nextYear,nextMonth));        //下个月
        datas.add(new MonthTimeEntity(nextYear2,nextMonth2));      //下下个月
        adapter = new MonthTimeAdapter(datas,getActivity());
        reycycler.setAdapter(adapter);

    }

    private void initView() {

    }

    public void onEventMainThread(UpdataCalendar event) {
        adapter.notifyDataSetChanged();
        startTime.setText(startDay.getMonth()+"月"+startDay.getDay()+"日"+"\n");
        if (stopDay.getDay() == -1) {
            stopTime.setText("退房"+"\n"+"日期");
        }else{
            stopTime.setText(stopDay.getMonth() + "月" + stopDay.getDay() + "日" + "\n");
        }
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        EventBus.getDefault().unregister(this);
    }
}