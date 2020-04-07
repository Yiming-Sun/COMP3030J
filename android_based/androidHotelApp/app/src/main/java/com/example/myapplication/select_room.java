package com.example.myapplication;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ImageView;
import android.widget.Spinner;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class select_room extends AppCompatActivity {

    private TextView getTime1;
    private TextView getTime2;
    private ImageView seascene;
    private ImageView bigbed;
    private ImageView twopeoplesea;
    private TextView roomnumber1;
    private TextView roomnumber2;
    private TextView roomnumber3;
    private Spinner sp1;
    private String str1;
    private Spinner sp2;
    private String str2;
    private Spinner sp3;
    private String str3;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_select_room);

        Intent intent = getIntent();
        getTime1 = findViewById(R.id.getTime1);
        getTime2 = findViewById(R.id.getTime2);
        getTime1.setText(intent.getStringExtra("startTime"));
        getTime2.setText(intent.getStringExtra("stopTime"));
        roomnumber1 = findViewById(R.id.roomnumber1);
        roomnumber2 = findViewById(R.id.roomnumber2);
        roomnumber3 = findViewById(R.id.roomnumber3);

        sp1 = (Spinner) findViewById(R.id.spinner);

        sp2 = (Spinner) findViewById(R.id.spinner2);

        sp3 = (Spinner) findViewById(R.id.spinner3);

        sp1.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                str1 = parent.getItemAtPosition(position).toString();
                roomnumber1.setText(str1);
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });

        sp2.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                str2 = parent.getItemAtPosition(position).toString();
                roomnumber2.setText(str2);
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });

        sp3.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                str3 = parent.getItemAtPosition(position).toString();
                roomnumber3.setText(str3);
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });

        seascene = findViewById(R.id.seascene);
        bigbed = findViewById(R.id.bigbed);
        twopeoplesea = findViewById(R.id.twopeoplesea);

        seascene.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new AlertDialog.Builder(select_room.this).setTitle("支付提醒").setMessage("您选择的海景房，请支付。")
                        .setNegativeButton("确定", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                Intent intent = new Intent(select_room.this,show_order.class);
                                intent.putExtra("startTime",getTime1.getText());
                                intent.putExtra("stopTime",getTime2.getText());
                                intent.putExtra("roomnumber",roomnumber1.getText());
                                intent.putExtra("room","海景房");
                                startActivity(intent);
                            }
                        })
                        .setPositiveButton("取消", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {

                            }
                        }).show();
            }
        });

        bigbed.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new AlertDialog.Builder(select_room.this).setTitle("支付提醒").setMessage("您选择的普通大床房，请支付。")
                        .setNegativeButton("确定", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                Intent intent = new Intent(select_room.this,show_order.class);
                                intent.putExtra("startTime",getTime1.getText());
                                intent.putExtra("stopTime",getTime2.getText());
                                intent.putExtra("roomnumber",roomnumber2.getText());
                                intent.putExtra("room","普通大床房");
                                startActivity(intent);
                            }
                        })
                        .setPositiveButton("取消", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {

                            }
                        }).show();
            }
        });

        twopeoplesea.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new AlertDialog.Builder(select_room.this).setTitle("支付提醒").setMessage("您选择的双人海景房，请支付。")
                        .setNegativeButton("确定", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                Intent intent = new Intent(select_room.this,show_order.class);
                                intent.putExtra("startTime",getTime1.getText());
                                intent.putExtra("stopTime",getTime2.getText());
                                intent.putExtra("roomnumber",roomnumber3.getText());
                                intent.putExtra("room","双人海景房");
                                startActivity(intent);
                            }
                        })
                        .setPositiveButton("取消", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {

                            }
                        }).show();
            }
        });



    }
}
