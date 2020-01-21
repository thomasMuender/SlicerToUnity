using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DataExchangeFormat
{
  public string identifier; // DICOM Datensatz

  // Headset
   public Vector3 headpos; // Position x,y,z
   public Matrix4x4 headrot; // Rotation (4x4 Transform-Matrix by Slicer)
  
  
  // Controller1
  public Vector3 ctr1pos;  // Position x,y,z
  public Matrix4x4 ctr1rot;   // Rotation 

  // Controller2
  public Vector3 ctr2pos;  // Position x,y,z
  public Matrix4x4 ctr2rot;   // Rotation 

  public int stackno; // Stacknummer
  public int imgno; // Bildnummer

  //public float contrast; // Kontrast (ggf. nach pull)


}
