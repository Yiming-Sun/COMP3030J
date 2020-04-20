package com.example.myapplication;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class Database extends SQLiteOpenHelper {


    // Database Version
    static final int DATABASE_VERSION = 1;

    // Database Name
    static final String DATABASE_NAME = "blogdb";
    // Contacts table name
    // table name
    static final String Customer_TABLE = "customer";
    // Contacts Table Columns names
    public static final String KEY_ID = "id";

    public static final String KEY_USERNAME = "username";

    public Database(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }


    @Override
    public void onCreate(SQLiteDatabase db) {
        String sql = "create table " + Customer_TABLE + " ( "
                + KEY_ID + " integer primary key , "
                + KEY_USERNAME + " text,"
//                +  + " text, "
//                +  + " text "
                + " ) ";

        db.execSQL(sql);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS " + Customer_TABLE);
        onCreate(db);
    }
}
