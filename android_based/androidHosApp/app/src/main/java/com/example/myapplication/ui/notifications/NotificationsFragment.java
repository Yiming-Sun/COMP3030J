package com.example.myapplication.ui.notifications;

import android.app.AlertDialog;
import android.app.TimePickerDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.TimePicker;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProviders;

import com.example.myapplication.R;

import java.util.Calendar;

public class NotificationsFragment extends Fragment {
    private TextView tuifang;
    private TextView roomService;
    private NotificationsViewModel notificationsViewModel;
    private Calendar c = Calendar.getInstance();

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        notificationsViewModel =
                ViewModelProviders.of(this).get(NotificationsViewModel.class);
        View root = inflater.inflate(R.layout.fragment_notifications, container, false);

        tuifang = root.findViewById(R.id.tuifang);
        tuifang.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new AlertDialog.Builder(getActivity()).setTitle("退房提醒").setMessage("您确定要退房吗？")
                        .setNegativeButton("确定", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {

                            }
                        })
                        .setPositiveButton("取消", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {

                            }
                        }).show();
            }
        });



        roomService = root.findViewById(R.id.roomService);
        roomService.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                c.setTimeInMillis(System.currentTimeMillis());
                int mHour = c.get(Calendar.HOUR_OF_DAY);
                int mMinute = c.get(Calendar.MINUTE);
                new TimePickerDialog(getActivity(),AlertDialog.THEME_HOLO_LIGHT,new TimePickerDialog.OnTimeSetListener() {
                    @Override
                    public void onTimeSet(TimePicker view, int hourOfDay, int minute) {
                        c.setTimeInMillis(System.currentTimeMillis());
                        c.set(Calendar.HOUR_OF_DAY, hourOfDay);
                        c.set(Calendar.MINUTE, minute);
                        if(minute<10){
                            roomService.setText("预约打扫时间"+hourOfDay+":"+"0"+minute);
                        }else{
                            roomService.setText("预约打扫时间"+hourOfDay+":"+minute);
                        }
                    }
                }, mHour, mMinute, true).show();
            }
        });

        return root;
    }
}