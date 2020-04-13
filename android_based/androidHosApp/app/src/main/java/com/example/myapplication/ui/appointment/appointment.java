package com.example.myapplication.ui.appointment;


import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
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


public class appointment extends AppCompatActivity implements View.OnClickListener {
    private Button Submit_button;
    private Button mButton1;
    private Button mButton2;
    private Button mButton3;
    private Button mButton4;
    private Button mButton5;
    private Button mButton6;
    private Button mButton7;
    private boolean city = false;
    private boolean petType = false;
    private boolean Time = false;
    private boolean app_type = false;
    private boolean docotr = false;

    Fragment fragment = null;
    FragmentManager fragmentManager = getSupportFragmentManager();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_appointment);
        Submit_button = findViewById(R.id.Submit);
        mButton1 =  findViewById(R.id.PetType);
        mButton2 = findViewById(R.id.City);
        mButton3 = findViewById(R.id.Doc);
        mButton4 = findViewById(R.id.Date);
        mButton5 = findViewById(R.id.PetName);
        mButton6 = findViewById(R.id.Time);
        mButton7 = findViewById(R.id.appType);
        mButton1.setOnClickListener(this);
        mButton2.setOnClickListener(this);
        mButton3.setOnClickListener(this);
        mButton4.setOnClickListener(this);
        mButton5.setOnClickListener(this);
        mButton6.setOnClickListener(this);
        mButton7.setOnClickListener(this);
        Submit_button.setOnClickListener(this);
    }

//    public boolean test(){
//        new  Thread(){
//            public  void run(){
//                try {
////                    Log.i("调试","sssss");
//                    String driver = "com.mysql.jdbc.Driver";
//
//                    Log.i("cnm","samfan");
////                    String url = "jdbc:jtds:sqlserver://49.235.31.130:8000/blogdb/customer";
//                    String url = "jdbc:mysql://cdb-6jo4m3hi.bj.tencentcdb.com:10019/score";
////                    Connection conn = DriverManager.getConnection(url, "root", "wywcj123");
////                    "jdbc:mysql://cdb-6jo4m3hi.bj.tencentcdb.com:10019/score";
//                    Class.forName("com.mysql.jdbc.Driver");
//                    Connection conn = DriverManager.getConnection(url, "root", "wywcj123");
////                    Connection conn = DriverManager.getConnection(url, "", "");
//                    Log.i("是吧","samfan");
//                    if(conn!=null){
//                        Log.i("success","ccccccccccccccc");
//                        Statement stmt = conn.createStatement();
//                        String sql = "select name from score" ; //要sql
////                        String sql = "select username from customer" ; //要sql
////                        stmt.executeUpdate(sql);
//                        ResultSet st= stmt.executeQuery(sql);
////                        String s= st.getString(1);
////                        Log.i("所有",s);
//                        while(st.next()){
//                            //有数据
//                            //取数据:getXXX
//                            String id = st.getString(1);//获得第一列的值
//                            //int id rs.getInt("id");// 获得id列的值
//                            Log.i("所有",id+"==>");
//                            //rs.gettimestamp(columnIndex)
//                        }
//                    }else{
//                        Log.i("wrong","wwwwwwwwwwwwwwwwww");
//                    }
//                } catch (ClassNotFoundException e) {
//                    e.printStackTrace();
//                } catch (SQLException e) {
//                    e.printStackTrace();
//                }
//            }
//        }.start();
//        return false;
//    }

    public boolean test() {
        new Thread() {
            public void run() {
                try {
//                    Log.i("调试","sssss");
                    String driver = "com.mysql.jdbc.Driver";

                    Log.i("cnm", "samfan");
//                    String url = "jdbc:jtds:sqlserver://49.235.31.130:8000/blogdb/customer";
                    String url = "jdbc:mysql://cdb-ezakhzhc.cd.tencentcdb.com:10140/score";
//                    Connection conn = DriverManager.getConnection(url, "root", "wywcj123");
//                    "jdbc:mysql://cdb-6jo4m3hi.bj.tencentcdb.com:10019/score";
                    Class.forName("com.mysql.jdbc.Driver");
                    Connection conn = DriverManager.getConnection(url, "root", "xchS0806!0920");
//                    Connection conn = DriverManager.getConnection(url, "", "");
                    Log.i("是吧", "samfan");
                    if (conn != null) {
                        Log.i("success", "ccccccccccccccc");
                        Statement stmt = conn.createStatement();

                        SharedPreferences userSettings1= getSharedPreferences("data", MODE_PRIVATE);
                        String username = userSettings1.getString("username", "");
                        Log.i("username",username);


                        SharedPreferences userSettings= getSharedPreferences("ymd", 0);
                        String year = userSettings.getString("year", "");
                        String month = userSettings.getString("month", "");
                        String day = userSettings.getString("day", "");
                        String date = year +"/"+ month +"/" + day;
                        Log.i("date",date);


                        String phone = null;
                        String nickname = null;

                        String getphone = "select phone from customer where username='"+username+"'"; //要sql
                        ResultSet st = stmt.executeQuery(getphone);
                        while(st.next()){
                            //有数据
                            //取数据:getXXX
                            phone = st.getString(1);//获得第一列的值
                            //int id rs.getInt("id");// 获得id列的值
                            Log.i("phone", phone);
                        }

                        String getnickname = "select nickname from customer where username='"+username+"'"; //要sql
                        ResultSet st2 = stmt.executeQuery(getnickname);
                        while(st2.next()){
                            //有数据
                            //取数据:getXXX
                            nickname = st2.getString(1);//获得第一列的值
                            //int id rs.getInt("id");// 获得id列的值
                            Log.i("nickname",nickname);
                        }



                        String insert = "insert into new_appointment (petType, petName, date, applicant, phoneNo, appoint_time, user_id, app_type, doctor) values("+choice+", '"+PetName+"', '"+date+"', '"+nickname+"', '"+phone+"', '"+choiceTime+"', '"+username+"', '"+choiceappType+"', '"+choiceDoctor+"')"; //要sql
                        stmt.executeUpdate(insert);
                    } else {
                        Log.i("wrong", "wwwwwwwwwwwwwwwwww");
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

            case R.id.PetType:
                showpetdialog();
                break;

            case R.id.PetName:
                inputTitleDialog();
                break;

            case R.id.Time:
                showTimedialog();
                break;

            case R.id.appType:
                showPetTypedialog();
                break;

            case R.id.Doc:
                if (city == true){
                    showdoctor();
                } else{
                    Toast.makeText(appointment.this, getString(R.string.selsect_your_city_first), Toast.LENGTH_SHORT).show();
                }
                break;

            case R.id.Date:
                CalendarFragment calendarFragment = new CalendarFragment();
                calendarFragment.show(fragmentManager, "Calendar");
        }
    }

    int choice; //0 cat 1 dog
    int choiceTime;
    int choiceDoctor;
    int choiceappType; //0 normal 1 urgent
    String[] items;

    private void showPetTypedialog() {
        final String[] whichapptype = new String[]{"Normal", "Urgent"};
        AlertDialog.Builder singleChoiceDialog = new AlertDialog.Builder(appointment.this);
        singleChoiceDialog.setIcon(R.mipmap.touxiang);
        singleChoiceDialog.setTitle("select the appointment type");
        //第二个参数是默认的选项
        singleChoiceDialog.setSingleChoiceItems(whichapptype, 0, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                choiceappType = which;
            }
        });
        singleChoiceDialog.setPositiveButton("确定", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                if (choiceappType != -1) {
                    Toast.makeText(appointment.this,
                            "你选择了" + whichapptype[choiceappType],
                            Toast.LENGTH_SHORT).show();
                    app_type = true;
                }
            }
        });
        singleChoiceDialog.show();
    }



    private void showSingDialog() {
        items = new String[]{"shanghai", "chengndu", "beijing"};
        AlertDialog.Builder singleChoiceDialog = new AlertDialog.Builder(appointment.this);
        singleChoiceDialog.setIcon(R.mipmap.touxiang);
        singleChoiceDialog.setTitle("City");
        //第二个参数是默认的选项
        singleChoiceDialog.setSingleChoiceItems(items, 0, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                choice = which;
            }
        });
        singleChoiceDialog.setPositiveButton("确定", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                if (choice != -1) {
                    Toast.makeText(appointment.this,
                            "你选择了" + items[choice],
                            Toast.LENGTH_SHORT).show();
                    city = true;
                }
            }
        });
        singleChoiceDialog.show();
    }


    private void showdoctor() {
        final String[] whichDoctor = new String[]{"a", "b", "c"};
        AlertDialog.Builder singleChoiceDialog = new AlertDialog.Builder(appointment.this);
        singleChoiceDialog.setIcon(R.mipmap.touxiang);
        singleChoiceDialog.setTitle("select your doctor");
        //第二个参数是默认的选项
        singleChoiceDialog.setSingleChoiceItems(whichDoctor, 0, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                choiceDoctor = which;
            }
        });
        singleChoiceDialog.setPositiveButton("确定", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                if (choiceDoctor != -1) {
                    Toast.makeText(appointment.this,
                            "你选择了" + whichDoctor[choiceDoctor],
                            Toast.LENGTH_SHORT).show();
                    docotr = true;
                }
            }
        });
        singleChoiceDialog.show();
    }

    private void showpetdialog() {
        final String[] items = {"cat", "dog"};
        AlertDialog.Builder singleChoiceDialog = new AlertDialog.Builder(appointment.this);
        singleChoiceDialog.setIcon(R.mipmap.touxiang);
        singleChoiceDialog.setTitle("petType");
        //第二个参数是默认的选项
        singleChoiceDialog.setSingleChoiceItems(items, 0, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                choice = which;
            }
        });
        singleChoiceDialog.setPositiveButton("确定", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                if (choice != -1) {
                    Toast.makeText(appointment.this,
                            "你选择了" + items[choice],
                            Toast.LENGTH_SHORT).show();
                    petType = true;
                }
            }
        });
        singleChoiceDialog.show();
    }


    private void showTimedialog() {
        final String[] whichTime = {"8:00-10:00", "10:00-12:00", "13:00-15:00", "15:00-17:00"};
        AlertDialog.Builder singleChoiceDialog = new AlertDialog.Builder(appointment.this);
        singleChoiceDialog.setIcon(R.mipmap.touxiang);
        singleChoiceDialog.setTitle("Select your time");
        //第二个参数是默认的选项
        singleChoiceDialog.setSingleChoiceItems(whichTime, 0, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                choiceTime = which;
            }
        });
        singleChoiceDialog.setPositiveButton("确定", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                if (choiceTime != -1) {
                    Toast.makeText(appointment.this,
                            "你选择了" + whichTime[choiceTime],
                            Toast.LENGTH_SHORT).show();
                    Time = true;
                }
            }
        });
        singleChoiceDialog.show();
    }


    String PetName;

    private void inputTitleDialog() {

        final EditText inputServer = new EditText(this);
        inputServer.setFocusable(true);

        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle(getString(R.string.save)).setIcon(
                                R.mipmap.touxiang).setView(inputServer).setNegativeButton(
                                getString(R.string.cancel), null);
        builder.setPositiveButton(getString(R.string.ok),
                                new DialogInterface.OnClickListener() {
            public void onClick(DialogInterface dialog, int which) {
                       final String inputName = inputServer.getText().toString();
                       PetName = inputName;
                }
        });
        builder.show();
    }


}


