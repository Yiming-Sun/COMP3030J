package com.example.myapplication.ui.information;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import com.example.myapplication.R;
import com.example.myapplication.ui.appointment.appointment_details;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

public class InformationFragment extends Fragment {
    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        View root = inflater.inflate(R.layout.fragment_information, container, false);

        //Button button = root.findViewById(R.id.button);
        //button.setOnClickListener(new View.OnClickListener() {
        //@Override
        //public void onClick(View v) {
        //Intent intent = new Intent(getActivity(),Signin.class);
        //startActivity(intent);
        //}
        //});

        Button button = root.findViewById(R.id.My_Appointment);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getActivity(), appointment_details.class);
                startActivity(intent);
            }
        });


        return root;
    }

}
