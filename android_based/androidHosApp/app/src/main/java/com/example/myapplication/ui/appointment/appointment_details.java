package com.example.myapplication.ui.appointment;


import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.SimpleAdapter;

import com.example.myapplication.R;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import androidx.appcompat.app.AppCompatActivity;


public class appointment_details extends AppCompatActivity {

    private ListView Lv = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_appointment_details);


        Lv = findViewById(R.id.Lv);

        final String[] name = new String[]{"a", "b", "c"};
        final String[] message = new String[]{
                "a",
                "b",
                "c"};
        final int[] photo = new int[]{R.drawable.appointment, R.drawable.appointment, R.drawable.appointment};
        List<Map<String, Object>> data = new ArrayList<Map<String, Object>>();

        Map<String, Object> map1 = new HashMap<String, Object>();
        map1.put("photo", R.drawable.appointment);
        map1.put("name", name[0]);
        data.add(map1);

        Map<String, Object> map2 = new HashMap<String, Object>();
        map2.put("photo", R.drawable.appointment);
        map2.put("name", name[1]);
        data.add(map2);

        Map<String, Object> map3 = new HashMap<String, Object>();
        map3.put("photo", R.drawable.appointment);
        map3.put("name", name[2]);
        data.add(map3);

        Lv.setAdapter(new SimpleAdapter(this, data, R.layout.item, new String[]{"photo", "name"}, new int[]{R.id.iv, R.id.tv_name}));
        Lv.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> arg0, View arg1, int arg2, long arg3) {

                Bundle bundle = new Bundle();
                bundle.putInt("photo", photo[arg2]);
                bundle.putString("message", message[arg2]);
                Intent intent = new Intent();
                intent.putExtras(bundle);
                intent.setClass(appointment_details.this, MoveList.class);
                Log.i("message", message[arg2]);
                startActivity(intent);
            }
        });
    }


}

