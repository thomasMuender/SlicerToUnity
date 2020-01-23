using UnityEngine;

public class HelloClient : MonoBehaviour
{
    private HelloRequester _helloRequester;

    private void Start()
    {
        _helloRequester = new HelloRequester();
        _helloRequester.Start();
    }

    private void Update()
    {
        Vector3 pos = Camera.main.transform.position;
        Vector3 ang = Camera.main.transform.rotation.eulerAngles;
        Matrix4x4 m = Matrix4x4.TRS(new Vector3(-pos.x, -pos.z, pos.y) * 1000, Quaternion.Euler(ang.x, ang.z, -ang.y), Vector3.one);

        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                _helloRequester.dataPackage.t[j + (i * 4)] = m[i, j];

        if (Input.GetKeyDown(KeyCode.E)) _helloRequester.reqestData = true;
    }

    private void OnDestroy()
    {
        _helloRequester.Stop();
    }
}
