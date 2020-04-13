package com.example.myapplication;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Looper;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import androidx.appcompat.app.AppCompatActivity;

public class Signin extends AppCompatActivity {
    static boolean RIGHT = false;
    private EditText ed_username;
    private EditText ed_password;
    private Button bt_login;
    private Button bt_register;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);



        ed_username = findViewById(R.id.ed_username);
        ed_password = findViewById(R.id.ed_password);
        bt_login = findViewById(R.id.login);
        bt_register = findViewById(R.id.surface1_register_button);

        //给登录按钮注册监听器，实现监听器接口，编写事件
        bt_login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //获取用户输入的数据
                String strUsername = ed_username.getText().toString();
                String strPassword = ed_password.getText().toString();

                test(strUsername, strPassword);
            }
        });

        //给注册按钮写监听事件，跳转到注册界面
        bt_register.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Signin.this, Register.class);
                startActivity(intent);
            }
        });

    }

    public boolean test(final String a, final String b) {
        new Thread() {
            public void run() {
                try {
                    String url = "jdbc:mysql://cdb-ezakhzhc.cd.tencentcdb.com:10140/score";
                    Class.forName("com.mysql.jdbc.Driver");
                    Connection conn = DriverManager.getConnection(url, "root", "xchS0806!0920");
                    if (conn != null) {
                        Log.i("success", "连上了");
                        Statement stmt = conn.createStatement();

                        String get_username = "select username from customer where username="+a;
                        ResultSet UN = stmt.executeQuery(get_username);


                        String username = null;
                        while (UN.next()) {
                            username = UN.getString(1);
                            Log.i("名字", username);
                        }

                        final String get_password = "select password_hash from customer where username="+a;
                        ResultSet PH = stmt.executeQuery(get_password);

                        String password_hash = null;
                        while (PH.next()) {
                            password_hash = PH.getString(1);
                            Log.i("密码", password_hash);
                        }

                        if (a.equals(username) && b.equals(password_hash)) {
                            Log.i("登陆成功", username+password_hash);
                            Looper.prepare();
                            Toast.makeText(Signin.this, "用户名和密码正确！", Toast.LENGTH_SHORT).show();
                            Intent intent = new Intent(Signin.this, Hos.class);
                            SharedPreferences sp = getSharedPreferences("data", MODE_PRIVATE);
                            final SharedPreferences.Editor editor = sp.edit();
                            editor.putString("username", a);
                            editor.commit();
                            startActivity(intent);
                            Looper.loop();
                        }else{
                            Log.i("密码错误或是其他问题", username+password_hash);
                            Looper.prepare();
                            Toast.makeText(Signin.this, "用户名或密码错误！", Toast.LENGTH_SHORT).show();
                            Looper.loop();
                        }


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
}
