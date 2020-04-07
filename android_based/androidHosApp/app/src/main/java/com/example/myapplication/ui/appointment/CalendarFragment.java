package com.example.myapplication.ui.appointment;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.widget.CalendarView;
import android.widget.Toast;

import androidx.fragment.app.DialogFragment;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import com.example.myapplication.R;

public class CalendarFragment extends DialogFragment {

    SharedPreferences sharedPreferences;
    View v;
    CalendarView cv;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        // TODO Auto-generated method stub

        getDialog().requestWindowFeature(Window.FEATURE_NO_TITLE);
        v = inflater.inflate(R.layout.calender, container, false);
        cv=v.findViewById(R.id.calendarView);
        cv.setOnDateChangeListener(new CalendarView.OnDateChangeListener() {
            public void onSelectedDayChange(CalendarView view, int year, int month, int dayOfMonth) {
                sharedPreferences = getActivity().getSharedPreferences("ymd", 0);
                SharedPreferences.Editor editor = sharedPreferences.edit();
                editor.putString("year", Integer.toString(year));
                editor.putString("month", Integer.toString(month+1));
                editor.putString("day", change(dayOfMonth));
                editor.commit();
                Toast.makeText(getActivity(), "year: "+year+"month"+(month+1)+"day"+dayOfMonth, Toast.LENGTH_LONG).show();
                final FragmentManager fragmentManager = getFragmentManager();
                FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();
                getDialog().dismiss();
            }
        });
        setCancelable(true);
        return v;
    }
    public String change(int d){
        if(d<10){
            return "0"+d;
        }
        else{
            return String.valueOf(d);
        }
    }


}
