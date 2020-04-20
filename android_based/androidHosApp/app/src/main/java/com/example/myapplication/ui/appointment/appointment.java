package com.example.myapplication.ui.appointment;


import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.example.myapplication.R;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;


public class appointment extends AppCompatActivity implements View.OnClickListener{
    private Button Submit_button;
    private Button mButton1;
    private Button mButton2;
    private Button mButton3;
    private Button mButton4;
    private boolean city = false;

    Fragment fragment = null;
    FragmentManager fragmentManager = getSupportFragmentManager();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_appointment);
        Submit_button=(Button) findViewById(R.id.Submit);
        mButton1 = (Button) findViewById(R.id.My_Pet);
        mButton2 = (Button) findViewById(R.id.City);
        mButton3 = (Button) findViewById(R.id.Doc);
        mButton4 = (Button) findViewById(R.id.Date);
        mButton1.setOnClickListener(this);
        mButton2.setOnClickListener(this);
        mButton3.setOnClickListener(this);
        mButton4.setOnClickListener(this);
        Submit_button.setOnClickListener(this);
    }

    public boolean test(){
        new  Thread(){
            public  void run(){
                try {
//                    Log.i("调试","sssss");
                    String driver = "com.mysql.jdbc.Driver";

                    Log.i("cnm","samfan");
                    String url = "jdbc:mysql://49.235.31.130:7777/blogdb/customer";
//                    String url = "jdbc:mysql://cdb-6jo4m3hi.bj.tencentcdb.com:10019/score";
//                    Connection conn = DriverManager.getConnection(url, "root", "wywcj123");
//                    "jdbc:mysql://cdb-6jo4m3hi.bj.tencentcdb.com:10019/score";
                    Class.forName("com.mysql.jdbc.Driver");
//                    Connection conn = DriverManager.getConnection(url, "root", "wywcj123");
                    Connection conn = DriverManager.getConnection(url, "", "");
                    Log.i("是吧","samfan");
                    if(conn!=null){
                        Log.i("success","ccccccccccccccc");
                        Statement stmt = conn.createStatement();
                        String sql = "select username from customer" ; //要sql
//                        stmt.executeUpdate(sql);
                        ResultSet st= stmt.executeQuery(sql);
//                        String s= st.getString(1);
//                        Log.i("所有",s);
                        while(st.next()){
                            //有数据
                            //取数据:getXXX
                            String id = st.getString(1);//获得第一列的值
                            //int id rs.getInt("id");// 获得id列的值
                            Log.i("所有",id+"==>");
                            //rs.gettimestamp(columnIndex)
                        }
                    }else{
                        Log.i("wrong","wwwwwwwwwwwwwwwwww");
                    }
                } catch (ClassNotFoundException e) {
                    e.printStackTrace();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }.start();
        return false;
    }

    @Override
    public void onClick(View view) {
        switch (view.getId()) {
            case R.id.Submit:
                test();
//                Toast.makeText(this, "lianjie", Toast.LENGTH_SHORT).show();
                break;

            case R.id.City:

                showSingDialog();
                break;
            case R.id.Date:
                CalendarFragment calendarFragment = new CalendarFragment();
                calendarFragment.show(fragmentManager, "Calendar");
        }
    }

    int choice;
    private void showSingDialog(){
        final String[] items = {"shanghai","chengndu","beijing"};
        AlertDialog.Builder singleChoiceDialog = new AlertDialog.Builder(appointment.this);
        singleChoiceDialog.setIcon(R.drawable.touxiang);
        singleChoiceDialog.setTitle("City");
        //第二个参数是默认的选项
        singleChoiceDialog.setSingleChoiceItems(items, 0, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                choice= which;
            }
        });
        singleChoiceDialog.setPositiveButton("确定", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                if (choice!=-1){
                    Toast.makeText(appointment.this,
                            "你选择了" + items[choice],
                            Toast.LENGTH_SHORT).show();
                    city=true;
                }
            }
        });
        singleChoiceDialog.show();
    }


        }


