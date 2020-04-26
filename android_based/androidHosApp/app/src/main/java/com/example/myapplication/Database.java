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
<<<<<<< HEAD
    static final String Employee_TABLE = "employee";
    static final String Answer_question_TABLE = "answer_question";
    static final String ID_TABLE = "id";
    static final String New_appointment_TABLE = "new_appointment";
    static final String Question_TABLE = "question";
    // Contacts Table Columns names
    public static final String KEY_ID = "id";
    public static final String KEY_USERNAME = "username";
    public static final String KEY_PASSWORD_HASH = "password_hash";
    public static final String KEY_EMAIL = "email";
    public static final String KEY_PHONE = "phone";
    public static final String KEY_NICKNAME = "nickname";
    public static final String KEY_GENDER = "gender";
    public static final String KEY_CITY = "city";
    public static final String KEY_ADDRESS = "address";
    public static final String KEY_NATIONALITY = "nationality";
    public static final String KEY_PERSONALITY_SIGNATURE = "personal_signature";
    public static final String KEY_TIMES = "times";
    public static final String KEY_EMID = "emid";
    public static final String KEY_WORKPLACE = "workplace";
    public static final String KEY_ANIMAL = "animal";
    public static final String KEY_CID = "cid";
    private static final String KEY_APPLICANT = "applicant";
    private static final String KEY_DATE = "date";
    private static final String KEY_APPOINT_TIME = "appoint_time";
    private static final String KEY_PETTYPE = "ket_petType";
    private static final String KEY_PETNAME = "pet_name";
    private static final String KEY_DOCTOR = "doctor";
    private static final String KEY_PHONENO = "phoneNo";
    private static final String KEY_COMMENT = "comment";
    private static final String KEY_CONDITION = "condition";
    private static final String KEY_OP_DATE = "op_date";
    private static final String KEY_OP_TIME = "op_time";
    private static final String KEY_APP_TYPE = "app_type";
    private static final String KEY_USER_ID = "user_id";

=======
    // Contacts Table Columns names
    public static final String KEY_ID = "id";

    public static final String KEY_USERNAME = "username";
>>>>>>> 937ceb6fe6d7ad31becf0929e01472a1db7965fa

    public Database(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }


    @Override
    public void onCreate(SQLiteDatabase db) {
<<<<<<< HEAD
        String customer = "create table " + Customer_TABLE + " ( "
                + KEY_ID + " integer primary key , "
                + KEY_USERNAME + " text,"
                + KEY_PASSWORD_HASH + " text, "
                + KEY_EMAIL + " text, "
                + KEY_PHONE + " text, "
                + KEY_NICKNAME + " text, "
                + KEY_GENDER + " integer, "
                + KEY_CITY + " text, "
                + KEY_ADDRESS + " text, "
                + KEY_NATIONALITY + " text, "
                + KEY_PERSONALITY_SIGNATURE + " text, "
                + KEY_TIMES + " integer "
                + " ) ";

        String employee = "create table " + Employee_TABLE + " ( "
                + KEY_ID + " integer primary key , "
                + KEY_USERNAME + " text,"
                + KEY_PASSWORD_HASH + " text, "
                + KEY_EMAIL + " text, "
                + KEY_EMID + " text, "
                + KEY_PHONE + " text, "
                + KEY_ANIMAL + " text, "
                + KEY_WORKPLACE + " text, "
                + KEY_NICKNAME + " text, "
                + KEY_GENDER + " integer, "
                + KEY_CITY + " text, "
                + KEY_ADDRESS + " text, "
                + KEY_NATIONALITY + " text, "
                + KEY_PERSONALITY_SIGNATURE + " text, "
                + KEY_TIMES + " integer "
                + " ) ";


        String id = "create table " + ID_TABLE+ " ( "
                + KEY_ID + " integer primary key , "
                + KEY_CID + " text "
                + " ) ";

        String new_appointment = "create table " + New_appointment_TABLE + " ( "
                + KEY_ID + " integer primary key , "
                + KEY_APPLICANT + " text,"
                + KEY_DATE + " text, "
                + KEY_APPOINT_TIME + " integer, "
                + KEY_PETTYPE + " integer, "
                + KEY_PETNAME + " text, "
                + KEY_DOCTOR + " integer, "
                + KEY_PHONENO + " text, "
                + KEY_COMMENT + " text, "
                + KEY_CONDITION + " text, "
                + KEY_OP_DATE + " text, "
                + KEY_OP_TIME + " Integer, "
                + KEY_APP_TYPE + " text, "
                + KEY_USER_ID + " text "
                + " ) ";


        String question = "create table " + Question_TABLE + " ( "
                + KEY_ID + " integer primary key , "
                + KEY_USERNAME + " text,"
                + KEY_PASSWORD_HASH + " text, "
                + KEY_EMAIL + " text, "
                + KEY_PHONE + " text, "
                + KEY_NICKNAME + " text, "
                + KEY_GENDER + " Integer, "
                + KEY_CITY + " text, "
                + KEY_ADDRESS + " text, "
                + KEY_NATIONALITY + " text, "
                + KEY_PERSONALITY_SIGNATURE + " text, "
                + KEY_TIMES + " Integer "
                + " ) ";


        String answer_question = "create table " + Answer_question_TABLE + " ( "
                + KEY_ID + " integer primary key , "
                + KEY_USERNAME + " text,"
                + KEY_PASSWORD_HASH + " text, "
                + KEY_EMAIL + " text, "
                + KEY_PHONE + " text, "
                + KEY_NICKNAME + " text, "
                + KEY_GENDER + " Integer, "
                + KEY_CITY + " text, "
                + KEY_ADDRESS + " text, "
                + KEY_NATIONALITY + " text, "
                + KEY_PERSONALITY_SIGNATURE + " text, "
                + KEY_TIMES + " Integer "
                + " ) ";

        db.execSQL(customer);
        db.execSQL(employee);
        db.execSQL(answer_question);
        db.execSQL(id);
        db.execSQL(new_appointment);
        db.execSQL(question);
=======
        String sql = "create table " + Customer_TABLE + " ( "
                + KEY_ID + " integer primary key , "
                + KEY_USERNAME + " text,"
//                +  + " text, "
//                +  + " text "
                + " ) ";

        db.execSQL(sql);
>>>>>>> 937ceb6fe6d7ad31becf0929e01472a1db7965fa
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS " + Customer_TABLE);
        onCreate(db);
    }
}
