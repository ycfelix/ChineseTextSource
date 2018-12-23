using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
 
using Android.App;
using Android.Content;
using Android.Content.Res;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using Newtonsoft.Json;

namespace Tes.Droid
{
    public class RadicalReader:MainActivity
    {
        public RawData GetSource(string bushou)
        {
            string content;
            string filename = bushou + @".json";
            AssetManager assets = this.Assets;
            using (StreamReader sr = new StreamReader(assets.Open(filename)))
            {
                content = sr.ReadToEnd();
            }
            RawData Sources = JsonConvert.DeserializeObject<RawData>(content);
            return Sources;
        }
    }

    public class RawData
    {
        [JsonProperty("fulltext")]
        public string[] Source { get; set; }


        [JsonProperty("title")]
        public string title { get; set; }
    }


}