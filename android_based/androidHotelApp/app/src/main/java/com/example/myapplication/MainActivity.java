package com.example.myapplication;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private EditText ed_username;
    private EditText ed_password;
    private Button bt_login;
    private Button bt_register;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        SharedPreferences sp = getSharedPreferences("data",MODE_PRIVATE);
        final SharedPreferences.Editor editor = sp.edit();

        ed_username = (EditText) findViewById(R.id.ed_username);
        ed_password = (EditText) findViewById(R.id.ed_password);
        bt_login = (Button) findViewById(R.id.login);
        bt_register = (Button) findViewById(R.id.surface1_register_button);

        //给登录按钮注册监听器，实现监听器接口，编写事件
        bt_login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //获取用户输入的数据
                String strUsername = ed_username.getText().toString();
                String strPassword = ed_password.getText().toString();


                //判断用户名和密码是否正确（为可以进行测试，暂时将用户名和密码都定义为admin）
                if(strUsername.equals("admin") && strPassword.equals("admin")){
                    Toast.makeText(MainActivity.this,"用户名和密码正确！",Toast.LENGTH_SHORT).show();
                    Intent intent = new Intent(MainActivity.this,Hotel.class);
                    editor.putString("username",strUsername);
                    editor.commit();
                    startActivity(intent);
                }else {
                    Toast.makeText(MainActivity.this,"用户名或密码错误！", Toast.LENGTH_SHORT).show();
                }
            }
        });

        //给注册按钮写监听事件，跳转到注册界面
        bt_register.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this,Register.class);
                startActivity(intent);
            }
        });

    }
}
