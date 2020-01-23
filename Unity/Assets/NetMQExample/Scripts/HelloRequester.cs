using NetMQ;
using NetMQ.Sockets;
using UnityEngine;
using System.Collections.Generic;

[System.Serializable]
public class Package
{
    public float[] t = new float[16];
}

public class HelloRequester : RunAbleThread
{
    public Package dataPackage = new Package();
    public bool reqestData = false;

    private SubscriberSocket SUB;
    private PublisherSocket PUB;
    private RequestSocket REQ;

    private List<byte[]> data = new List<byte[]>();

    protected override void Run()
    {
        AsyncIO.ForceDotNet.Force(); // this line is needed to prevent unity freeze after one use, not sure why yet

        using (SUB = new SubscriberSocket())
        using (PUB = new PublisherSocket())
        using (REQ = new RequestSocket()) {
            SUB.Connect("tcp://localhost:5555");
            SUB.Subscribe("");

            PUB.Connect("tcp://localhost:5556");

            REQ.Connect("tcp://localhost:5557");

            Debug.Log("Connected: Receiving Messages");

            while (Running) {

                /*Receive continuos Slicer data*/
                string msg = SUB.ReceiveFrameString();

                /*Send continuos Unity data*/
                var bytes = new byte[dataPackage.t.Length * 4];
                System.Buffer.BlockCopy(dataPackage.t, 0, bytes, 0, bytes.Length);
                PUB.SendFrame(bytes);

                /*Request volume data once*/
                if(reqestData) {
                    REQ.SendFrame("volume");
                    string msg2 = REQ.ReceiveFrameString();
                    Debug.Log(msg2);

                    byte[] file = System.IO.File.ReadAllBytes(msg2);
                    Debug.Log(file.Length);

                    int d1 = System.BitConverter.ToInt32(file, 0);
                    int d2 = System.BitConverter.ToInt32(file, 4);
                    int d3 = System.BitConverter.ToInt32(file, 8);
                    float[] volume = new float[d1 * d2 * d3];
                    System.Buffer.BlockCopy(file, 12, volume, 0, volume.Length * sizeof(float));

                    string s = d1+ " " + d2 + " " + d3 + " : ";
                    //for (int i = 0; i < volume.Length; ++i) s += volume[i] + " ";
                    Debug.Log(s);

                    reqestData = false;
                }

                /*60fps*/
                System.Threading.Thread.Sleep(16);
            }

            SUB.Close();
            PUB.Close();
            REQ.Close();
        }
        NetMQConfig.Cleanup();
    }

    protected override void Clean()
    {
        SUB.Close();
        PUB.Close();
        REQ.Close();
        NetMQConfig.Cleanup();
        AsyncIO.ForceDotNet.Force();
    }
}