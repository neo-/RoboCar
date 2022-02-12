package com.naveejr.robocar;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    private boolean appActive = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    protected void onResume() {
        super.onResume();
        appActive = true;

        new Thread(() -> {
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            if (appActive)
                startActivity(new Intent(MainActivity.this, RoboControllerActivity.class));
        }).start();

    }

    @Override
    protected void onPause() {
        appActive = false;
        super.onPause();
    }
}