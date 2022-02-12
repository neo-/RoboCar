package com.naveejr.robocar.network;

import retrofit2.Call;
import retrofit2.Response;
import retrofit2.http.Body;
import retrofit2.http.Header;
import retrofit2.http.POST;
import retrofit2.http.Query;

public interface DeviceControllerInterface {


    @POST("/robot")
    Call<Void> controlRobot(@Query("speed") float speed, @Query("direction") float direction);

}
