package com.naveejr.robocar.network;

import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.text.SimpleDateFormat;
import java.util.Locale;

import okhttp3.OkHttpClient;
import retrofit2.Retrofit;
import retrofit2.converter.jackson.JacksonConverterFactory;

public class DataService {

    private DeviceControllerInterface deviceControllerInterface;

    public DataService(){
        OkHttpClient.Builder builder = new OkHttpClient.Builder()
                .hostnameVerifier((hostname, session) -> true);


        OkHttpClient client = builder.build();

        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.setDateFormat(new SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.US));
        objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
        objectMapper.enable(DeserializationFeature.READ_UNKNOWN_ENUM_VALUES_AS_NULL);

        Retrofit retrofit1 = new Retrofit.Builder()
                .baseUrl("https://192.168.8.152:5000")
                .addConverterFactory(JacksonConverterFactory.create(objectMapper))
                .client(client)
                .build();

        deviceControllerInterface = retrofit1.create(DeviceControllerInterface.class);
    }

}
