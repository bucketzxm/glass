package edu.shu.shu_glass;

import android.bluetooth.BluetoothAdapter;
import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;

public class MainActivity extends ActionBarActivity {

    private Button openBlueToothBtn;

    public static boolean isBlueTeethOpened = false;

    private BlueToothService mBlueToothService;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        openBlueToothBtn = (Button)findViewById(R.id.openBlueToothBtn);
        openBlueToothBtn.setOnClickListener(listener);

    }

    private OnClickListener listener = new OnClickListener(){
        @Override
        public void onClick(View v){
//            Intent intent = new Intent(MainActivity.this,BlueToothService.class);
//            switch (v.getId()){
//                case R.id.openBlueToothBtn:
//                    startService(intent);
//            }

            BluetoothAdapter adapter = BluetoothAdapter.getDefaultAdapter();
            int state = adapter.getState();
            if (state == BluetoothAdapter.STATE_OFF) {
                adapter.enable();

            }else if (state == BluetoothAdapter.STATE_ON) {
//                do nothing
            }

        }

    };


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
}
