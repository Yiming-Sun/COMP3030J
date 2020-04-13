package com.example.myapplication.ui.home;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageButton;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.example.myapplication.R;
import com.example.myapplication.ui.appointment.appointment;
import com.example.myapplication.ui.doctor.doctor_details;

public class HomeFragment extends Fragment {

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        View root = inflater.inflate(R.layout.fragment_home, container, false);

        //Button button = root.findViewById(R.id.button);
        //button.setOnClickListener(new View.OnClickListener() {
        //@Override
        //public void onClick(View v) {
        //Intent intent = new Intent(getActivity(),Signin.class);
        //startActivity(intent);
        //}
        //});

        ImageButton button = root.findViewById(R.id.ruzhu);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getActivity(), appointment.class);
                startActivity(intent);
            }
        });

        ImageButton doc1 = root.findViewById(R.id.doc1);
        doc1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getActivity(), doctor_details.class);
                startActivity(intent);
            }
        });

        ImageButton doc2 = root.findViewById(R.id.doc2);
        doc2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getActivity(), doctor_details.class);
                startActivity(intent);
            }
        });

        ImageButton doc3 = root.findViewById(R.id.doc3);
        doc3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getActivity(), doctor_details.class);
                startActivity(intent);
            }
        });


        return root;
    }
}