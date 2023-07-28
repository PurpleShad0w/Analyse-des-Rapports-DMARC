package fr.ac6;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Dictionary;
import java.util.Enumeration;
import java.util.Hashtable;
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
    public static void main(String[] args) throws IOException {
        test();
    }

    public static void request(String path, Dictionary<String, String> parameters) throws IOException
    {
        HttpClient httpclient = HttpClients.createDefault();
        String default_path = "http://localhost/post/";
        String host_path = default_path.concat(path);
        HttpPost httppost = new HttpPost(host_path);
        
        Integer dict_size = parameters.size();
        List<NameValuePair> params = new ArrayList<NameValuePair>(dict_size);
        Enumeration<String> k = parameters.keys();

        while (k.hasMoreElements()) {
            String key = k.nextElement();
            String value = parameters.get(key);
            params.add(new BasicNameValuePair(key, value));
        }
        
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

    public static void test() throws IOException
    {
        String test_path = "post.php";
        Dictionary<String, String> test_parameters = new Hashtable<>();
        test_parameters.put("macAddress", "mac_test");
        test_parameters.put("licenseFeature", "feature_test");

        request(test_path, test_parameters);
    }
}