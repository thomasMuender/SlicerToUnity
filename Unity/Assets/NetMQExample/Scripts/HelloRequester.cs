using NetMQ;
using NetMQ.Sockets;
using UnityEngine;

/// <summary>
///     Example of requester who only sends Hello. Very nice guy.
///     You can copy this class and modify Run() to suits your needs.
///     To use this class, you just instantiate, call Start() when you want to start and Stop() when you want to stop.
/// </summary>
public class HelloRequester : RunAbleThread
{

    protected override void Run()
    {
        AsyncIO.ForceDotNet.Force(); // this line is needed to prevent unity freeze after one use, not sure why yet
        using (SubscriberSocket client = new SubscriberSocket())
        {
            client.Connect("tcp://localhost:5556");
            client.Subscribe("");
            Debug.Log("Connected");
            while (Running)
            {
                    string message = null;
                    bool gotMessage = false;
                    while (Running)
                    {
                        gotMessage = client.TryReceiveFrameString(out message); // this returns true if it's successful
                        if (gotMessage) break;
                    }

                    if (gotMessage) {
                        Debug.Log(message);
                    }
            }
            client.Close();
        }
        NetMQConfig.Cleanup();
    }

    protected override void Clean()
    {

    }
}