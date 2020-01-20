using UnityEngine;
using System.Collections.Generic;
using System.IO;
using System.Globalization;

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
 
    }

    private void OnDestroy()
    {
        _helloRequester.Stop();
    }
}
