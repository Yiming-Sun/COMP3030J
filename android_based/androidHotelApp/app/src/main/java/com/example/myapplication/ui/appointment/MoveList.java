package com.example.myapplication.ui.appointment;



import android.app.Activity;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import com.example.myapplication.R;

public class MoveList extends Activity {

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.model);

        Bundle bundle=getIntent().getExtras();
        int id=bundle.getInt("photo");
        String message=bundle.getString("message");
        ImageView Iv=(ImageView) findViewById(R.id.Iv);
        Iv.setImageResource(id);
        TextView tv=(TextView) findViewById(R.id.tv_message);
        tv.setText(message);


    }

}
