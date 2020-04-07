package com.example.myapplication;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class show_order extends AppCompatActivity {

    private TextView room;
    private TextView startTime;
    private TextView stopTime;
    private  TextView roomnumber;
    private  TextView username;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_show_order);

        SharedPreferences sp = getSharedPreferences("data",MODE_PRIVATE);

        Intent intent = getIntent();
        room = findViewById(R.id.room);
        startTime = findViewById(R.id.startTime);
        stopTime = findViewById(R.id.stopTime);
        roomnumber = findViewById(R.id.roomnumber);
        username = findViewById(R.id.username);

        username.setText(sp.getString("username",""));
        room.setText(intent.getStringExtra("room"));
        startTime.setText(intent.getStringExtra("startTime"));
        stopTime.setText(intent.getStringExtra("stopTime"));
        roomnumber.setText(intent.getStringExtra("roomnumber"));


    }
}


