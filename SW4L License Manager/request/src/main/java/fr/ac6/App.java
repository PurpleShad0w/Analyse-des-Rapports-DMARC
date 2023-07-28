package fr.ac6;

import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import org.apache.commons.io.IOUtils;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicNameValuePair;


public class App 
{
    public static void main( String[] args ) throws IOException, UnsupportedEncodingException
    {
        HttpClient httpclient = HttpClients.createDefault();
        HttpPost httppost = new HttpPost("http://localhost/post/post.php");
        
        List<NameValuePair> params = new ArrayList<NameValuePair>(2);
        params.add(new BasicNameValuePair("macAddress", "mac_test"));
        params.add(new BasicNameValuePair("licenseFeature", "feature_test"));
        httppost.setEntity(new UrlEncodedFormEntity(params, "UTF-8"));
        
        HttpResponse response = httpclient.execute(httppost);
        HttpEntity entity = response.getEntity();

        if (entity != null) {
            try (InputStream instream = entity.getContent()) {
                String result = IOUtils.toString(instream, StandardCharsets.UTF_8);
                System.out.println(result);
            }
        }
    }
}